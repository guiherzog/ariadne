int RXLED = 17;

/* Array of all buttons on the terminal */
int buttons[] = {16, 10,15, 14,5,3,4};
unsigned long lastMsgTime = 0;
int lastButtonPressed = 0;
void setup()
{
 pinMode(RXLED, OUTPUT);
 for (int i=0; i<7; i++){
  pinMode(buttons[i], INPUT_PULLUP);
 }
 Serial.begin(9600);
}

void loop()
{
 // Verifies if any button was pressed.
 for (int i=0; i<7; i++){
  if (digitalRead(buttons[i]) == LOW){
      // Send a serial message to be received by the CoreTerminal
      // Adds a Debounce to avoid sending duplicate requests.
      if (millis() - lastMsgTime > 3000 || lastButtonPressed != i){
        Serial.print("FT_");
        Serial.println(i+1);
        digitalWrite(RXLED,LOW);        
        lastMsgTime = millis();
        lastButtonPressed = i;
      }
      
  }
 }
 
 digitalWrite(RXLED,HIGH);
}


