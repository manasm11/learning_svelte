<script>
	import FormElement from "../components/FormElement.svelte";
</script>

<main>
	<form>
		<FormElement name="First Name" required/>
		<FormElement name="Last Name"/>
		<br>
		<FormElement name="Email" type="email"/>
	</form>
</main>
