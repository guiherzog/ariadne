int RXLED = 17;

/* Array of all buttons on the terminal */
int buttons[] = {16, 10,15, 14,5,3,4};
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
 for (int i=0; i<7; i++){
  if (digitalRead(buttons[i]) == LOW){
      Serial.print("Button [");
      Serial.print(i+1);
      Serial.println("] pressed");
      digitalWrite(RXLED,LOW);
  }
 }
 
 digitalWrite(RXLED,HIGH);
}


