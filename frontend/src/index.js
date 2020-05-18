import React from 'react';
import ReactDOM from 'react-dom';
import ViewportSize from "react-viewport-size";
import { Provider } from 'react-redux';

import App from 'pages';
import { ServiceWorker } from 'shared/common';
import ReduxStore from 'reduxstore';

import 'shared/scss/index.scss';


ReactDOM.render(
    <Provider store={ReduxStore}>
        <App/>
        <ViewportSize corner='top-left' />
    </Provider>,
    document.getElementById('root')
);

ServiceWorker.unregister();
