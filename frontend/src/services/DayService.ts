import { api } from "../api/axios";

export class DayService {


  static async listDays(){
    const response = await api.get('/days')
    return response.data
  }
}