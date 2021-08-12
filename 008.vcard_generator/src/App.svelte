<!-- https://github.com/PacktPublishing/Sveltejs-3-and-Sapper-Projects -->

<script>
	import Navbar from "./Sections/Navbar.svelte";
	import VCard from "./Sections/VCard.svelte";
	import Form from "./UI/Form.svelte";
	const title = "vCard Generator";
	let QRCode = "";
</script>

<Navbar {title} />
<main>
	<Form on:createQRCode={(e) => (QRCode = e.detail)} />
	<VCard {QRCode}/>
</main>

<style>
	main {
		max-width: 600px;
		padding: 1rem;
		margin: 0 auto;
	}
</style>