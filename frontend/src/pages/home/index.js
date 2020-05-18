import React from 'react';
import { RequireLoggedUser, ReduxStateHOC, Logout } from "hocs";
import { CONSTANTS } from "shared/constants";
import { renderClasses } from "shared/common/functions";
import v from "voca";


class Home extends React.Component {
    componentDidMount() {
        this.props.fetchUserBasicData();
    }

    getOnClick = (label) => () => {
        this.props.fetchButtonClick(label);
    }

    renderCounters = (counters) => {
        return counters.map((button, i) => (
            <button
                className={renderClasses({
                    'pz-button': true,
                    'primary': i % 2 === 0
                })}
                key={i}
                onClick={this.getOnClick(button.label)}
                style={{
                    transform: `scale(${button.value / 50 + 1})`
                }}
            >
                Button {i + 1} <b>({button.value})</b>
            </button>
        ))
    };

    render() {
        if (this.props.auth.fetchBasicDataStatus === CONSTANTS.FETCH.SUCCESS) {
            const {counters} = this.props.auth.user.user;

            return (
                <main className='pz-page center'>
                    <section className='pz-page__content-user'>
                        <header className='pz-page__header'>
                            <img src={this.props.auth.user.app_logo} alt="logo" className='pz-page__logo'/>
                            <section>
                                <h1>{this.props.auth.user.app_title}</h1>
                                <p>{this.props.auth.user.app_description}</p>
                            </section>
                        </header>
                        <section className='grid-big-gap'>
                            <h1 className='text-center'>Welcome, <span className='primary'>{v.titleCase(this.props.auth.user.user.full_name)}</span></h1>
                            <section className='pz-page__buttons'>
                                {this.renderCounters(counters)}
                            </section>
                        </section>
                    </section>
                    <button className='pz-button primary pz-page__logout' onClick={this.props.logout}>Logout</button>
                </main>
            );
        }

        return (
            <main>

            </main>
        );
    }
}

export default ReduxStateHOC(RequireLoggedUser(Logout(Home)));