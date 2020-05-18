import React from 'react';
import { Logout, ReduxStateHOC, RequireAdminLoggedUser } from "hocs";
import moment from 'moment';
import v from 'voca';
import { ResponsivePie } from '@nivo/pie';
import { CONSTANTS } from "shared/constants";

const MyResponsivePie = ({data}) => (
    <ResponsivePie
        data={data}
        margin={{ top: 40, right: 80, bottom: 80, left: 80 }}
        innerRadius={0.25}
        padAngle={3}
        height={300}
        cornerRadius={5}
        colors={{ scheme: 'nivo' }}
        borderWidth={1}
        borderColor={{ from: 'color', modifiers: [ [ 'darker', 0.2 ] ] }}
        radialLabelsSkipAngle={10}
        radialLabelsTextXOffset={6}
        radialLabelsTextColor="#333333"
        radialLabelsLinkOffset={0}
        radialLabelsLinkDiagonalLength={16}
        radialLabelsLinkHorizontalLength={24}
        radialLabelsLinkStrokeWidth={1}
        radialLabelsLinkColor={{ from: 'color' }}
        slicesLabelsSkipAngle={10}
        slicesLabelsTextColor="#333333"
        animate={true}
        motionStiffness={90}
        motionDamping={15}
        defs={[
            {
                id: 'dots',
                type: 'patternDots',
                background: 'inherit',
                color: 'rgba(255, 255, 255, 0.3)',
                size: 4,
                padding: 1,
                stagger: true
            },
            {
                id: 'lines',
                type: 'patternLines',
                background: 'inherit',
                color: 'rgba(255, 255, 255, 0.3)',
                rotation: -45,
                lineWidth: 6,
                spacing: 10
            }
        ]}
        fill={[
            {
                match: {
                    id: 'Button 1'
                },
                id: 'dots'
            },
            {
                match: {
                    id: 'Button 2'
                },
                id: 'lines'
            }
        ]}
        legends={[
            {
                anchor: 'bottom',
                direction: 'row',
                translateY: 56,
                itemWidth: 100,
                itemHeight: 18,
                itemTextColor: '#999',
                symbolSize: 18,
                symbolShape: 'circle',
                effects: [
                    {
                        on: 'hover',
                        style: {
                            itemTextColor: '#000'
                        }
                    }
                ]
            }
        ]}
    />
);


class Admin extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            columns: [
                {field: 'id', name: 'id'},
                {field: 'full_name', name: 'Full name'},
                {field: 'username', name: 'Username'},
                {field: 'logged_at', name: 'Logged time'},
                {field: 'logout_at', name: 'Logout time'},
                {field: 'duration', name: 'Duration'},
                {field: 'button_1', name: 'Button 1'},
                {field: 'button_2', name: 'Button 2'},
            ]
        };
    }

    componentDidMount() {
        this.props.fetchUserBasicData();
        this.props.fetchUsers();
    }

    getSessionData = (session) => {
        if (!session) {
            return {
                logged_at: '',
                logout_at: '',
                duration: "User not logged yet",
            };
        }

        return {
            logged_at: moment(session.logged_at).format('LLL'),
            logout_at: session.logout_at ? moment(session.logout_at).format('LLL') : '',
            duration: session.duration !== -1 ? moment.utc(session.duration * 1000).format('HH:mm:ss') : "Session still active"
        };
    };

    getCountersData = (counters) => (
        counters.reduce((prev, counter) => ({
            ...prev,
            [counter.label]: counter.value
        }), {})
    );

    getUserData = (user) => ({
        id: user.id,
        full_name: user.full_name,
        username: user.username,
        ...this.getSessionData(user.session),
        ...this.getCountersData(user.counters)
    });

    renderHeader = () => {
        const  {columns} = this.state;
        const renderedColumns = columns.map((column, i) => {
            return (
                <th key={i}>{column.name}</th>
            );
        });
        return (
            <thead>
                <tr>{renderedColumns}</tr>
            </thead>
        );
    }

    renderRow = (user, r) => {
        const  {columns} = this.state;
        const renderedColumns = columns.map((column, c) => {
            return (
                <td key={c}>{user[column.field]}</td>
            );
        });
        return (
            <tr key={r}>{renderedColumns}</tr>
        );
    };

    renderBody = () => {
        const  {users} = this.props.auth;
        const rows = users.map((user, r) =>
            this.renderRow(this.getUserData(user), r)
        );

        return (
            <tbody>
                {rows}
            </tbody>
        );
    }

    getChartData1 = () => {
        const {users} = this.props.auth;
        const actions = users.reduce((prev, user) => {
            user.counters.forEach((counter) => {
                if (prev[counter.label]) {
                    prev[counter.label] += counter.value
                } else {
                    prev[counter.label] = counter.value
                }
            });
            return prev;
        }, {});
        return Object.keys(actions).map((label, i) => ({
            id: v.titleCase(label.replace('_', ' ')),
            label: label,
            value: actions[label]
        }));
    };

    render() {

        if (this.props.auth.fetchBasicDataStatus !== CONSTANTS.FETCH.SUCCESS) {
            return (<section />);
        }

        return (
            <main className='pz-page'>
                <h1>Welcome, <span className='primary'>{v.titleCase(this.props.auth.user.user.full_name)}</span></h1>
                <section className='scroll pz-page__content-admin'>
                    <section className='pz-page__graphs grid-column-gap'>
                        <MyResponsivePie data={this.getChartData1()} />
                    </section>
                    <section className='grid scroll'>
                        <table className='pz-table'>
                            {this.renderHeader()}
                            {this.renderBody()}
                        </table>
                    </section>
                </section>
                <button className='pz-button primary pz-page__logout' onClick={this.props.logout}>Logout</button>
            </main>
        );
    }
}

export default ReduxStateHOC(RequireAdminLoggedUser(Logout(Admin)));