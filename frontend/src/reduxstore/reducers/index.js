import {combineReducers} from "redux";
import ReduxAuth from "./auth";
import ReduxModal from "./modal";


export const initialState = {
    auth: ReduxAuth.defaultState,
    modal: ReduxModal.defaultState
};

export const actions = {
    auth: ReduxAuth.actions,
    modal: ReduxModal.actions
};

export const rootReducer = combineReducers({
    auth: ReduxAuth.reducer,
    modal: ReduxModal.reducer
});