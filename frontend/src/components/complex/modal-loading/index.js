import React from 'react';
import { Modal } from "components/common";
import { ReduxStateHOC } from "hocs";
import Loader from 'react-loaders';


class ModalLoading extends React.Component {
    render() {
        const {open} = this.props.modal;

        return (
            <Modal visible={open}>
                <section className='pz-modal-loading'>
                    <Loader type="pacman" />
                </section>
            </Modal>
        );
    }
}

export default ReduxStateHOC(ModalLoading);