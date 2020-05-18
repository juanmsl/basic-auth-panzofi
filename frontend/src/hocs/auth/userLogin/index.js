import React from 'react';
import API from "api";
import { Redirect } from 'react-router-dom';
import { ReduxStateHOC } from "hocs";
import { CONSTANTS } from "shared/constants";


const UserLogin = (Component) => {
    class LoadingLoginPage extends React.Component {
        render() {
            const {auth, fetchUserLogin} = this.props;

            if (API.auth.isLoggedIn()) {
                if (API.auth.isAdmin()) {
                    return <Redirect to={CONSTANTS.URLS.ADMIN_HOME}/>
                } else {
                    return <Redirect to={CONSTANTS.URLS.HOME}/>
                }
            }

            return (
                <Component
                    {...this.props}
                    login={fetchUserLogin}
                    errorMessage={auth.fetchLoginMessage}
                />
            );
        }
    }

    return ReduxStateHOC(LoadingLoginPage);
};

export default UserLogin;