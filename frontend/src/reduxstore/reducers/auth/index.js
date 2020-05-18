import { CONSTANTS } from "shared/constants";
import API from "api";


const defaultState = {
    data: {},
    user: {},
    users: [],

    fetchLoginStatus: CONSTANTS.FETCH.STANDBY,
    fetchLoginMessage: null,

    fetchBasicDataStatus: CONSTANTS.FETCH.STANDBY,
    fetchBasicDataMessage: null,

    fetchUsersStatus: CONSTANTS.FETCH.STANDBY,
    fetchUsersMessage: null,
};

const actionTypes = {
    USER_LOGIN_REQUEST: 'USER_LOGIN_REQUEST',
    USER_LOGIN_SUCCESS: 'USER_LOGIN_SUCCESS',
    USER_LOGIN_FAILED: 'USER_LOGIN_FAILED',

    USER_BASIC_DATA_REQUEST: 'USER_BASIC_DATA_REQUEST',
    USER_BASIC_DATA_SUCCESS: 'USER_BASIC_DATA_SUCCESS',
    USER_BASIC_DATA_FAILED: 'USER_BASIC_DATA_FAILED',

    USER_USERS_REQUEST: 'USER_USERS_REQUEST',
    USER_USERS_SUCCESS: 'USER_USERS_SUCCESS',
    USER_USERS_FAILED: 'USER_USERS_FAILED',
};

const actions = {
    fetchUserLogin: (data) => (dispatch) => {
        dispatch({type: actionTypes.USER_LOGIN_REQUEST});

        const callback = (auth, response) => {
            if(auth) {
                console.info('auth :: fetchUserLogin :: success');
                dispatch({type: actionTypes.USER_LOGIN_SUCCESS, payload: response.data});
            } else {
                console.error('auth :: fetchUserLogin :: error');
                const message = response.response ? response.response.data.non_field_errors[0] : 'Something its happening with the server';
                dispatch({type: actionTypes.USER_LOGIN_FAILED, payload: message});
            }
        };

        API.auth.login(data, callback);
    },

    fetchUserBasicData: () => (dispatch) => {
        dispatch({type: actionTypes.USER_BASIC_DATA_REQUEST});

        const successCallback = (response) => {
            console.info('auth :: fetchUserBasicData :: success');
            dispatch({type: actionTypes.USER_BASIC_DATA_SUCCESS, payload: response.data});
        }

        const errorCallback = (response) => {
            console.error('auth :: fetchUserBasicData :: error');
            const message = response.response ? response.response.data.detail : 'Something its happening with the server';
            dispatch({type: actionTypes.USER_BASIC_DATA_FAILED, payload: message});
        }

        API.app.getBasicData(successCallback, errorCallback);
    },

    fetchButtonClick: (label) => (dispatch, getState) => {
        const successCallback = (response) => {
            console.info('auth :: fetchButtonClick :: success');
            const user = getState().auth.user;
            user.user.counters = user.user.counters.map((counter) => {
                if (counter.label === label) {
                    return response.data;
                }
                return counter;
            });
            dispatch({type: actionTypes.USER_BASIC_DATA_SUCCESS, payload: user});
        }

        const errorCallback = (response) => {
            console.error('auth :: fetchButtonClick :: error');
        }

        API.app.buttonClick(label, successCallback, errorCallback);
    },

    fetchUsers: () => (dispatch) => {
        dispatch({type: actionTypes.USER_USERS_REQUEST});

        const successCallback = (response) => {
            console.info('auth :: fetchUsers :: success');
            dispatch({type: actionTypes.USER_USERS_SUCCESS, payload: response.data});
        }

        const errorCallback = (response) => {
            console.error('auth :: fetchUsers :: error');
            const message = response.response ? response.response.data.detail : 'Something its happening with the server';
            dispatch({type: actionTypes.USER_USERS_FAILED, payload: message});
        }

        API.app.getUsers(successCallback, errorCallback);
    }
};

const reducer = (state = defaultState, action) => {
    switch (action.type) {
        case actionTypes.USER_LOGIN_REQUEST:
            return {
                ...state,
                fetchLoginStatus: CONSTANTS.FETCH.PROGRESS,
                fetchLoginMessage: 'Login in progress'
            };
        case actionTypes.USER_LOGIN_SUCCESS:
            return {
                ...state,
                fetchLoginStatus: CONSTANTS.FETCH.SUCCESS,
                fetchLoginMessage: defaultState.fetchLoginMessage,
                data: action.payload
            };
        case actionTypes.USER_LOGIN_FAILED:
            return {
                ...state,
                fetchLoginStatus: CONSTANTS.FETCH.FAILED,
                fetchLoginMessage: action.payload,
                data: defaultState.data
            };

        case actionTypes.USER_BASIC_DATA_REQUEST:
            return {
                ...state,
                fetchBasicDataStatus: CONSTANTS.FETCH.PROGRESS,
                fetchBasicDataMessage: 'Getting basic data'
            };
        case actionTypes.USER_BASIC_DATA_SUCCESS:
            return {
                ...state,
                fetchBasicDataStatus: CONSTANTS.FETCH.SUCCESS,
                fetchBasicDataMessage: defaultState.fetchBasicDataMessage,
                user: action.payload
            };
        case actionTypes.USER_BASIC_DATA_FAILED:
            return {
                ...state,
                fetchBasicDataStatus: CONSTANTS.FETCH.FAILED,
                fetchBasicDataMessage: action.payload,
                user: defaultState.user
            };

        case actionTypes.USER_USERS_REQUEST:
            return {
                ...state,
                fetchUsersStatus: CONSTANTS.FETCH.PROGRESS,
                fetchUsersMessage: 'Getting users'
            };
        case actionTypes.USER_USERS_SUCCESS:
            return {
                ...state,
                fetchUsersStatus: CONSTANTS.FETCH.SUCCESS,
                fetchUsersMessage: defaultState.fetchUsersMessage,
                users: action.payload
            };
        case actionTypes.USER_USERS_FAILED:
            return {
                ...state,
                fetchUsersStatus: CONSTANTS.FETCH.FAILED,
                fetchUsersMessage: action.payload,
                users: defaultState.user
            };

        default:
            return state;
    }
};

export default {
    defaultState,
    actionTypes,
    actions,
    reducer
};