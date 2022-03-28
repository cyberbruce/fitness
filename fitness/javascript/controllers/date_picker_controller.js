 
import { Controller } from "@hotwired/stimulus"
import flatpickr from "flatpickr";

export default class extends Controller {

  connect() {     
    if (this.data.get('time') == null) {
      flatpickr(this.element, {enableTime: false,});
      return;
    }

    
    let timeEnabled =  this.data.get('time').toString().toLowerCase() == "true";
    flatpickr(this.element, {enableTime: timeEnabled,});
    
  }
}