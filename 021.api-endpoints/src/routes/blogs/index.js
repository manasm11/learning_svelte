export function get(req) {
    console.log(req)
    return {
        body: [
            {id: 1, title: "Title1", content: "Content slkfjvndsfcv"},
            {id: 2, title: "Title2", content: "Content2 slkfjvndsfcv"},
        ],
        headers: {
            authentication: "Somekj ij"
        }
    }
}

export function post(req) {
    console.log(req)
    return {}
}

export function $delete(req) {
    console.log(req)
    return {}
}