<template>
  <div>
    <MovieListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
      class="col-2"
    />
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'
export default {
    name: 'MovieList',
    components: {
      MovieListItem,
    },
    computed: {
      movies() {
        return this.$store.state.movies
      }
    }
}
</script>

<style>
</style>