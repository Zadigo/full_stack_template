import { computed, ref, watchEffect } from "vue"

export function useDarkMode () {
    const darkMode = ref(false)

    const darkModeClasses = computed(() => {
        return [
            darkMode.value ? 'bg-dark text-light' : 'bg-white text-dark'
        ]
    })

    watchEffect(() => {
        var body = document.querySelector('body')
        if (darkMode.value) {
            body.classList.add('bg-dark')
            body.classList.add('text-light')
            body.classList.remove('bg-white')
            body.classList.remove('text-dark')
        } else {
            body.classList.add('bg-white')
            body.classList.add('text-dark')
            body.classList.remove('bg-dark')
            body.classList.remove('text-light')
        }
    })
    
    function toggleDarkMode () {
        darkMode.value = !darkMode.value
    }

    return {
        darkMode,
        toggleDarkMode,
        darkModeClasses
    }
}
