import { writable } from 'svelte/store';
import { capitalizeFirstLetter } from '$utilities/string';

const pokemons = writable([])

async function getPokemons() {
    const url = (offset, limit) => `https://pokeapi.co/api/v2/pokemon?limit=${limit}&offset=${offset}`
    const res = await fetch(url(0, 898));
    const data = await res.json();
    const pokemons_ = data.results.map((p, i: number) => {
        return {
            name: capitalizeFirstLetter(p.name),
            id: i + 1,
            image: `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${i + 1}.png`,
        }
    })
    pokemons.set(pokemons_)
}
getPokemons()

export default pokemons