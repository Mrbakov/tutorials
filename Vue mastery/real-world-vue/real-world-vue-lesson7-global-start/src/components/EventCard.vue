<template>
  <ul>
    <li v-for="(event, index) in events" :key="index">
      <div class="event-card -shadow">
        <span class="eyebrow">@{{ event.time }} on {{ event.date }}</span>
        <h4 class="title">{{ event.title }}</h4>
        <BaseIcon name="users" />
        <span>{{ event.attendees.length }} attending</span>
      </div>
      <router-link class="event-link" :to="{ name: 'event-show', params: { id: event.id, event: event } }">
        <h5>Go to event</h5>
      </router-link>
    </li>
  </ul>
</template>

<script>
export default {
  props: {
    events: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      // event: {
      //   id: 1,
      //   title: 'Beach Cleanup',
      //   date: 'Tues Aug 19, 2018',
      //   time: '6:00',
      //   attendees: [
      //     { id: 'abc123', name: 'Adam Jahr' },
      //     { id: 'def456', name: 'Gregg Pollack' }
      //   ]
      // }
    }
  }
}
</script>

<style scoped>
.event-card {
  padding: 20px;
  margin-bottom: 24px;
  transition: all 0.2s linear;
  cursor: pointer;
}
.event-card:hover {
  transform: scale(1.01);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2), 0 1px 15px 0 rgba(0, 0, 0, 0.19);
}
.event-card > .title {
  margin: 0;
}
.event-link {
  color: black;
  text-decoration: none;
  font-weight: 100;
}
</style>
