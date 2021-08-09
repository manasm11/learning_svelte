<script>
	import {count} from './cutom_stores'
</script>

<h1>Count : {$count}</h1>
<button on:click={count.increment}>INCREMENT</button>
<button on:click={count.decrement}>DECREMENT</button>
<button on:click={count.reset}>RESET</button>