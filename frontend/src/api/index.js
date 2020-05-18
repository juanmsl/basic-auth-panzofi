import AuthAPI from './auth';
import AdminAPI from './app';
import axios from "axios";


const axiosInstances = {
    auth: axios.create({
        baseURL: process.env.REACT_APP_BASIC_AUTH_SERVICES_URL,
        timeout: process.env.REACT_APP_REQUESTS_TIMEOUT
    }),
    app: axios.create({
        baseURL: process.env.REACT_APP_BASIC_AUTH_SERVICES_URL,
        timeout: process.env.REACT_APP_REQUESTS_TIMEOUT
    })
};

export default {
    auth: new AuthAPI(axiosInstances.auth),
    app: new AdminAPI(axiosInstances.app)
};