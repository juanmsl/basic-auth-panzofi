import React from 'react';
import {BrowserRouter, Route, Switch} from "react-router-dom";
import {TransitionGroup, CSSTransition} from "react-transition-group";
import Home from "pages/home";
import Login from "pages/login";
import Admin from "pages/admin";
import { ModalLoading } from "components";


const App = () => (
    <BrowserRouter>
        <Route render={({location}) => (
            <TransitionGroup className='transition-group'>
                <CSSTransition
                    key={location.key}
                    timeout={{enter: 300, exit: 300}}
                    classNames="fade"
                >
                    <Switch location={location}>
                        <Route path='/auth/login' exact><Login /></Route>
                        <Route path='/admin/' exact><Admin /></Route>
                        <Route path='/' exact><Home /></Route>
                    </Switch>
                </CSSTransition>
            </TransitionGroup>
        )}/>
        <ModalLoading />
    </BrowserRouter>
);

export default App;