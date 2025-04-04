import type {SearchRequest} from "@/model/searchRequest.js";
import axios from "axios";

const fetchOperadoras = async (searchParam: string, searchValue: string, desiredPage: Number | undefined) => {
    const requestPayload: SearchRequest = {
    search: searchParam,
    value: searchValue
  };
  try {
    const params = {
      page: String(desiredPage ? Number(desiredPage) : 1),
      per_page: String(20)
    };
    const response = await axios.post('/api/operadoras/search/', requestPayload,   {
        params: {
          page: params.page.toString(),
          per_page: params.per_page.toString()
        }
      });
    return response.data;
  } catch (error: any) {
    return 'Error fetching data: ' + error.message;
  }
}

export { fetchOperadoras };