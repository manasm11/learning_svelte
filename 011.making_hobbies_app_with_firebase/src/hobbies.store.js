import { writable } from "svelte/store";

var username = 'test'
const hobbies = writable([])
const BASE_URL = 'https://svelte-hobbies-firebase-default-rtdb.firebaseio.com'
const hobbiesURL = () => `${BASE_URL}/${username}/hobbies.json`
const getHobbyDeleteURL = id => `${BASE_URL}/${username}/hobbies/${id}.json`

const updateFromAPI = async (uname) => {
    if (uname) username = uname
    console.log(uname)
    let res = await fetch(hobbiesURL())
    let data = await res.json()
    let h = []
    for (const k in data) h.push({ id: k, value: data[k] })
    hobbies.set(h)
}

export default {
    ...hobbies,
    updateFromAPI,
    addHobby: async (hobby, uname) => {
        if (uname) username = uname
        let res = await fetch(hobbiesURL(), {
            method: 'POST',
            body: JSON.stringify(hobby),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        let data = await res.json()
        let newHobby = { id: data.name, value: hobby }
        hobbies.update(items => [newHobby, ...items])
    },

    deleteHobby: async (id, uname) => {
        if (uname) username = uname
        fetch(getHobbyDeleteURL(id), {
            method: 'DELETE'
        })
        hobbies.update(items => { items.splice(items.findIndex(i => i.id === id), 1); return items })
    }

}