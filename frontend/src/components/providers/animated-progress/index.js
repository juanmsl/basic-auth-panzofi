import React from "react";
import { Animate } from "react-move";


class AnimatedProgressProvider extends React.Component {
    static defaultProps = {
        valueStart: 0
    };

    constructor(props) {
        super(props);
        this.state = {
            isAnimated: false
        };
        this.interval = undefined
    }

    toggleIsAnimated = () => this.setState({isAnimated: !this.state.isAnimated});

    componentDidMount() {
        if (this.props.repeat) {
            this.interval = window.setInterval(
                this.toggleIsAnimated,
                this.props.duration
            );
        } else {
            this.toggleIsAnimated()
        }
    }

    componentWillUnmount() {
        if (this.interval) {
            window.clearInterval(this.interval);
        }
    }

    render() {
        return (
            <Animate
                start={() => ({
                    value: this.props.valueStart
                })}
                update={() => ({
                    value: [
                        this.state.isAnimated ? this.props.valueEnd : this.props.valueStart
                    ],
                    timing: {
                        duration: this.props.duration,
                        ease: this.props.easingFunction
                    }
                })}
            >
                {({value}) => this.props.children(value)}
            </Animate>
        );
    }
}

export default AnimatedProgressProvider;
