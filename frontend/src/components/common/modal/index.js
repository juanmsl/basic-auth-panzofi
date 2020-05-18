import React from 'react';
import ReactDOM from 'react-dom';

const modalRoot = document.getElementById('modal-root');


class Modal extends React.Component {
    constructor(props) {
        super(props);
        this.el = document.createElement('div');
    }

    componentDidMount() {
        modalRoot.appendChild(this.el);
    }

    componentWillUnmount() {
        modalRoot.removeChild(this.el);
    }

    render() {
        const {visible} = this.props
        return ReactDOM.createPortal(
            visible ? this.props.children : null,
            this.el
        );
    }
}

export default Modal;