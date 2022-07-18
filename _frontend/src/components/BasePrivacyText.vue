<template>
    <p>
        By providing your information you agree to our 
        <router-link :to="{ name: 'terms_of_condition' }" class="font-weight-bold">
            Privacy policy
        </router-link>
    </p>
</template>

<script>
export default {
    name: 'BasePrivacyText'
}
</script>
