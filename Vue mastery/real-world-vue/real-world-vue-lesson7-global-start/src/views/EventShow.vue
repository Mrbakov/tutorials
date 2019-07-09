<template>
  <div>
    <h1>Showing event #{{ id }}</h1>
    <h3>{{ event.title }}</h3>
  </div>
</template>
<script>
export default {
  props: ['id', 'event']
}
</script>
