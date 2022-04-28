const lsa = window.localStorage
export default {
  getItem(key) {
    try {
      return JSON.parse(lsa.getItem(key))
    } catch (err) {
      return null
    }
  },
  setItem(key, val) {
    lsa.setItem(key, JSON.stringify(val))
  },
  clear() {
    lsa.clear()
  },
  keys() {
    return lsa.keys()
  },
  removeItem(key) {
    lsa.removeItem(key)
  }
}