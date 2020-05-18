import React from "react";
import {connect} from 'react-redux';
import {actions} from "reduxstore/reducers";


const ReduxStateHOC = (Component) => {
    class ReduxStateContainer extends React.Component {
        render() {
            return (
                <Component {...this.props}/>
            );
        }
    }

    const mapStateToProps = (state) => (
        Object.keys(state).reduce((prev, current) => ({
                ...prev,
                [current]: state[current]
        }), {})
    );

    const actionsToDispatch = Object.keys(actions).reduce((prev, current) => {
        const reducerActions = actions[current];
        return {
            ...prev,
            ...reducerActions
        };
    }, {});

    return connect(
        mapStateToProps,
        actionsToDispatch
    )(ReduxStateContainer);
};

export default ReduxStateHOC;