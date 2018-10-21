int outputPin0 = 0;
int outputPin1 = 1;
int outputPin2 = 2;
int outputPin3 = 3;
int outputPin4 = 4;
int outputPin5 = 5;
int outputPin6 = 6;
int outputPin7 = 7;

int buttonPin0 = 8;
int buttonState0 = 0;
int buttonPin1 = 9;
int buttonState1 = 0;

int micPin = A0;    
int micValue = 0;
int tempPin = A1;
int tempValue = 0;
  

int button0HeldTime = 0;
int button1HeldTime = 0;
int pinStates[8] = {0};
void setup() 
{
  Serial.begin(9600);
  pinMode(buttonPin0, INPUT);
  pinMode(buttonPin1, INPUT);
  pinMode(13, OUTPUT);
  for(int i = 0; i < 8; i++)
  {
    pinMode(i, OUTPUT);
  }
}

void loop()
{
  // read the value from the sensor:
  micValue = analogRead(micPin);
  tempValue = analogRead(tempPin);
  buttonState0 = digitalRead(buttonPin0);
  buttonState1 = digitalRead(buttonPin1);
  if(buttonState0)
    digitalWrite(12, HIGH);
  else
    digitalWrite(12, LOW);

  if(buttonState1)
    digitalWrite(13, HIGH);
  else
    digitalWrite(13, LOW);

  
  if(micValue < 0)
    micValue *= -1;

  
    
    
  char output = (char) (((micValue % 256) * (tempValue % 256)) % 256);
//  Serial.println((micValue));
  for(int i = 0; i < 8; i++)
    pinStates[i] = bitRead(output, i);

  int sum = 0;
  for(int i = 0; i < 8; i++)
  {
    if(pinStates[i] == 1)
      digitalWrite(i, LOW);
    else
      digitalWrite(i, HIGH);
     
      
    Serial.print((!pinStates[i]) * (i + 1));
    Serial.print(",");
    sum += pinStates[i];
  }
  Serial.println(sum + 10);
  
}
