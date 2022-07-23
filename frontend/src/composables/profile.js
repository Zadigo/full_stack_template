import { ref } from 'vue'
import profileFields from '@/data/profile.json'

export default function useProfileComposable () {
  const fields = ref(profileFields)

  function getFields (name) {
    const data = fields.value[name]
    return data
  }
  return {
    getFields
  }
}
