import React from 'react';
import API from "api";
import {Redirect} from "react-router-dom";
import { CONSTANTS } from "shared/constants";

const RequireLoggedUser = (Component) => (
    props => (
        API.auth.isLoggedIn() ?
            <Component {...props} />
            :
            <Redirect to={CONSTANTS.URLS.LOGIN} />
    )
);

export default RequireLoggedUser;