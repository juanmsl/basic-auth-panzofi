import {createStore, compose, applyMiddleware} from "redux";
import thunk from 'redux-thunk';
import {rootReducer, initialState} from './reducers';


export default createStore(
    rootReducer,
    initialState,
    compose(applyMiddleware(thunk))
);