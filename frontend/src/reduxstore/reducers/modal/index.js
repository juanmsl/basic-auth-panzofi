
const defaultState = {
    open: false
};

const actionTypes = {
    MODAL_OPEN: 'MODAL_OPEN',
    MODAL_CLOSE: 'MODAL_CLOSE'
};

const actions = {
    openModal: () => (dispatch) => {
        dispatch({
            type: actionTypes.MODAL_OPEN
        });
    },
    closeModal: () => (dispatch) => {
        dispatch({
            type: actionTypes.MODAL_CLOSE
        });
    }
};

const reducer = (state = defaultState, action) => {
    switch (action.type) {
        case actionTypes.MODAL_OPEN:
            return {
                ...state,
                open: true
            };
        case actionTypes.MODAL_CLOSE:
            return {
                ...state,
                open: false
            };

        default:
            return state;
    }
};

export default {
    defaultState,
    actionTypes,
    actions,
    reducer
};