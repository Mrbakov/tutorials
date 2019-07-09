<template>
  <div>
    <h1>Events Listing</h1>
    <EventCard :events="events" />
    <BaseIcon />
  </div>
</template>

<script>
import EventCard from '@/components/EventCard.vue'

export default {
  components: {
    EventCard
  },
  data() {
    return {
      events: [
        {
          id: 1,
          title: 'Beach Cleanup',
          date: 'Tues Aug 19, 2018',
          time: '6:00',
          attendees: [
            { id: 'abc123', name: 'Adam Jahr' },
            { id: 'def456', name: 'Gregg Pollack' }
          ]
        },
        {
          id: 2,
          title: 'Testing test',
          date: 'Tues Aug 19, 2018',
          time: '18:00',
          attendees: [
            { id: 'abc123', name: 'Adam Jahr' },
            { id: 'def456', name: 'Gregg Pollack' }
          ]
        }
      ],
      id: null,
      title: null,
      date: null,
      time: null,
      attendees: []
    }
  },
  methods: {
    // pushEvents() {
    //   let event = {
    //     id: this.id,
    //     title: this.title,
    //     date: this.date,
    //     time: this.time,
    //     attendees: this.attendees
    //   }
    //   this.events.push(event)
    //   ;(this.id = null),
    //     (this.title = null),
    //     (this.date = null),
    //     (this.time = null),
    //     (this.attendees = [])
    // }
  }
}
</script>
