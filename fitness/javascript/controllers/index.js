import { Application } from "@hotwired/stimulus";
import DatePickerController from "./date_picker_controller";
import ChartsController from "./charts_controller";

stimulus = Application.start();
stimulus.register("datepicker", DatePickerController);
stimulus.register("charts", ChartsController);
