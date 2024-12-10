import { ref } from 'vue'
import profileFields from '@/data/profile.json'

/** Simplifies the usage of fields in user pofile */
export default function useProfileComposable () {
  const fields = ref(profileFields)

  /** 
   * Gets a set of fields for a
   * a given view
   */
  function getFields (name) {
    const data = fields.value[name]
    return data
  }

  /** Get initial values for a profile form */
  function getInitialValues (name, target) {
    const values = {}
    const fields = getFields(name)
    fields.forEach((field) => {
      values[field.name] = target[field.name]
    })
    return values
  }

  return {
    getFields,
    getInitialValues
  }
}
