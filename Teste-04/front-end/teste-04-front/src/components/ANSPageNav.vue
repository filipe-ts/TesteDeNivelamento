<script setup lang="ts">
import {fetchOperadoras} from "@/services/fetchOperadoras.ts";

const props = defineProps({
  pagination: {
    type: Object,
    required: true,
  },
  searchType: {
    type: String,
    required: true,
  },
  searchString: {
    type: String,
    required: true,
  }
})

const emit = defineEmits(['response']);

const nextPage = async () => {
  const response = await fetchOperadoras(props.searchType, props.searchString, props.pagination.current_page + 1);
  emit('response', response);
}

const prevPage = async () => {
  const response = await fetchOperadoras(props.searchType, props.searchString, props.pagination.current_page - 1);
  emit('response', response);
}
</script>

<template>
<nav :class="props.pagination.total_pages > 1 ? 'pageSelector' : 'transparent' ">
    <button class="btn" :disabled="!pagination.has_previous"
            @click="prevPage">
      <
    </button>
    {{ pagination.current_page}} / {{ pagination.total_pages}}
    <button class="btn" :disabled="!pagination.has_next"
            @click="nextPage">
      >
    </button>
  </nav>
</template>

<style scoped>
.none{
  display: none;
}
.pageSelector{
  display: flex;
  gap: 1rem;
  color: #ffffff;
}

.btn{
  background-color: #55ec93;
}
</style>