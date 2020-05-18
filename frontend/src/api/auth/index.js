import NProgress from "nprogress";
import Store from 'reduxstore';
import { actions } from 'reduxstore/reducers';
import API from "api/index";


class Interceptors {
    static requests = [];

    static RequestHandler = (request) => {
        Interceptors.requests.push(request.url);
        NProgress.start();
        NProgress.inc();
        Store.dispatch(actions.modal.openModal())
        return request;
    };

    static ErrorHandler = (error) => {
        Interceptors.requests.pop();
        if (Interceptors.requests.length === 0) {
            NProgress.done();
            Store.dispatch(actions.modal.closeModal())
        }
        const {status} = error.response;
        if (status === 401 || status === 403) {
            API.auth.logout(false);
        }
        return Promise.reject({...error});
    };

    static SuccessHandler = (response) => {
        Interceptors.requests.pop();
        if (Interceptors.requests.length === 0) {
            NProgress.done();
            Store.dispatch(actions.modal.closeModal())
        }
        return response
    };
}

class AuthAPI {

    constructor(http) {
        this.http = http;

        this.http.interceptors.request.use(
            Interceptors.RequestHandler
        );

        this.http.interceptors.response.use(
            Interceptors.SuccessHandler,
            Interceptors.ErrorHandler
        );
    }

    login = (data, callBack) => {
        this.getToken(data, (authenticated, response) => {

            if (authenticated) {
                const {token, is_admin} = response.data;
                localStorage.token = token;
                localStorage.is_admin = is_admin;

                if (callBack) callBack(true, response);
            } else {
                if (callBack) callBack(false, response);
            }
        });
    };

    isLoggedIn = () => {
        return !!localStorage.token;
    };

    isAdmin = () => {
        return localStorage.is_admin === "true";
    };

    logout = (doRequest = true, successCallback = undefined, errorCallback = undefined) => {
        if (doRequest) {
            this.http.post('/auth/logout', {}, {
                headers: {
                    'Authorization': `token ${localStorage.token}`
                }
            }, {loader: true}).then(function (response) {
                localStorage.clear();
                if (successCallback) successCallback(response);
            }).catch(function (error) {
                if (errorCallback) errorCallback(error);
            });
        } else {
            localStorage.clear();
        }
    };

    getToken = (data, callBack) => {
        this.http.post('/auth/token', data)
            .then(function (response) {
                if (callBack) callBack(true, response);
            }).catch(function (error) {
                if (callBack) callBack(false, error);
            });
    };
}

export default AuthAPI;