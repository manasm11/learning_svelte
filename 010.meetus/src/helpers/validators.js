export function isNotEmpty(value) {
    return !!value.trim()
}

export function isValidEmail(value) {
    return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(value)
}