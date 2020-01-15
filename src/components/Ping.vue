<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Ping',
  data() {
    return {
      msg: 'Hello!',
    }
  },
  methods: {
    async getMessage() {
      const path = 'http://localhost:5000/events'
      const result = await axios.get(path)
      console.log('res: ', result)
      this.msg = result.data
    },
  },
  created() {
    this.getMessage()
  },
}
</script>
