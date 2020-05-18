import React from 'react';
import {withRouter} from "react-router-dom";
import API from "api";
import {CONSTANTS} from "shared/constants";


const Logout = (Component) => {
    class LogoutHOC extends React.Component {
        logout = () => {
            const {history} = this.props;
            API.auth.logout(true, () => {
                history.push(CONSTANTS.URLS.LOGIN);
            });
        };

        render() {
            return <Component {...this.props} logout={this.logout} />
        }
    }

    return withRouter(LogoutHOC);
};

export default Logout;