import NProgress from "nprogress";
import Store from 'reduxstore';
import { actions } from 'reduxstore/reducers';
import API from "api";


class Interceptors {
    static requests = [];

    static RequestHandler = (request) => {
        request.headers['Authorization'] = `token ${localStorage.token}`;
        Interceptors.requests.push(request.url);
        if (!request.url.startsWith('/user/count/')) {
            NProgress.start();
            NProgress.inc();
            Store.dispatch(actions.modal.openModal())
        }
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

class AppAPI {

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

    getUsers = (successCallback, errorCallBack) => {
        this.http.get('/users')
            .then(function (response) {
                if (successCallback) successCallback(response);
            }).catch(function (error) {
                if (errorCallBack) errorCallBack(error);
            });
    };

    getBasicData = (successCallback, errorCallBack) => {
        this.http.get('/user/basicdata')
            .then(function (response) {
                if (successCallback) successCallback(response);
            }).catch(function (error) {
                if (errorCallBack) errorCallBack(error);
            });
    };

    buttonClick = (label, successCallback, errorCallBack) => {
        this.http.put(`/user/count/${label}`)
            .then(function (response) {
                if (successCallback) successCallback(response);
            }).catch(function (error) {
                if (errorCallBack) errorCallBack(error);
            });
    };
}

export default AppAPI;