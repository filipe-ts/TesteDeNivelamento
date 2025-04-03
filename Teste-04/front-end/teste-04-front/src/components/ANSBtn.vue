<script setup lang="ts">
import {computed, ref, watch} from "vue";
import { searchTypes } from "@/model/searchTypes.ts";
import axios from 'axios'
import type { SearchRequest } from "@/model/searchRequest";

const props = defineProps({
  searchType:{
    type: String,
    required: true,
  },
  searchString: {
    type: String,
    required: true,
  },
  desiredPage: {
    type: Number,
    required: false
  }
})

const emit = defineEmits(['response', 'error'])

const responseData = ref(null);
const errorMessage = ref('');

const fetchData = async () => {
    const requestPayload: SearchRequest = {
    search: props.searchType,
    value: props.searchString
  };
  try {
    const params = {
      page: String(props.desiredPage ? Number(props.desiredPage) : 1),
      per_page: String(20)
    };
    const response = await axios.post('/api/operadoras/search/', requestPayload,   {
        params: {
          page: params.page.toString(),
          per_page: params.per_page.toString()
        }
      });
    responseData.value = response.data;
  } catch (error: any) {
    errorMessage.value = 'Error fetching data: ' + error.message;
  }
}


const invalidCNPJSearchs = ["000", "0001"];
const isSearchEnable = computed(() => {
  if (props.searchType !== searchTypes.CNPJ && props.searchString.length > 2) {
    return true
  }

  if (props.searchType === searchTypes.CNPJ && !invalidCNPJSearchs.includes(props.searchString) && props.searchString.length > 2) {
    return true
  }

  return false
});

watch(responseData, () => {
  emit('response', responseData.value);
})

watch(errorMessage, () => {
  emit('error', errorMessage.value);
})
</script>

<template>
      <button @click="fetchData" :disabled="!isSearchEnable">
        Buscar
      </button>
</template>

<style scoped>

</style>