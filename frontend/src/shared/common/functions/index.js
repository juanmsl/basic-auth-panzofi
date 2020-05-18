

export const renderClasses = (classes) => (
    Object.keys(classes).filter(key => (
        classes[key]
    )).map(key => key).join(" ")
);
