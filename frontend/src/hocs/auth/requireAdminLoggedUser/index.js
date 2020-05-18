import React from 'react';
import API from "api";
import {Redirect} from "react-router-dom";
import { CONSTANTS } from "shared/constants";

const RequireAdminLoggedUser = (Component) => (
    props => {
        if (API.auth.isAdmin()) {
            return <Component {...props} />
        } else if (API.auth.isLoggedIn()) {
            return <Redirect to={CONSTANTS.URLS.HOME}/>
        } else {
            return <Redirect to={CONSTANTS.URLS.LOGIN}/>
        }
    }
);

export default RequireAdminLoggedUser;