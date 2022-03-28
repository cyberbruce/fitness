import { Application } from "@hotwired/stimulus";
import DatePickerController from "./date_picker_controller";

stimulus = Application.start()
stimulus.register("datepicker", DatePickerController)
