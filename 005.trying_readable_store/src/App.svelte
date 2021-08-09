<script>
	import {time} from './readable_store'
	const formatter = Intl.DateTimeFormat('en', {
		hour12: true,
		hour: "numeric",
		minute: "2-digit",
		second: "2-digit"
	})
</script>

<h1>{formatter.format($time)}</h1>