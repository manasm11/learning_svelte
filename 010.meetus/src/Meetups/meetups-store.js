import { writable } from "svelte/store";
import meetups_data from '../DummyData/meetups'

const meetups = writable(meetups_data)

export default {
    ...meetups,
    addMeetup: form_data =>
        meetups.update(m => [{ ...form_data, id: Math.random().toString() }, ...m]),
    toggleFavourite: id => meetups.update(m => {
        const obj = { ...m.find(meet => meet.id == id) }
        obj.isFavorite = !obj.isFavorite
        const newMeetups = [...m]
        newMeetups[m.findIndex(m => m.id == id)] = obj
        return newMeetups
    })
};
