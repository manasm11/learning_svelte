import { writable, get } from 'svelte/store'
import {v4} from 'uuid'

let items = writable([])
let _count = 0;

async function saveToAPI() {
    localStorage.setItem('todo-list', JSON.stringify(get(items)))
}

async function updateFromAPI() {
    items.set(JSON.parse(localStorage.getItem("todo-list")) || [])
}

export default {
    ...items,
    count: () => get(items).length,
    completed: () => get(items).filter(i => i.completed).length,
    updateFromAPI,
    saveToAPI,
    updateItem: item => items.update(l => {
        const temp = [...l];
        temp[l.findIndex(i => i.id === item.id)] = item;
        return temp;
    }) || saveToAPI(),
    deleteItem: id => items.update(l => l.filter(i => i.id !== id)) || saveToAPI(),
    addItem: text => items.update(l => l.concat({id: v4(), text, completed: false})) || saveToAPI(),
}