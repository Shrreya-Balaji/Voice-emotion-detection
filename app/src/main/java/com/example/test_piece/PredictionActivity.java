package com.example.test_piece;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.Window;
import android.view.WindowManager;
import android.widget.TextView;
import android.content.Intent;

public class PredictionActivity extends AppCompatActivity {
    TextView textView;

    @Override
    protected void onCreate(Bundle savedInstancestate) {
        super.onCreate(savedInstancestate);
        requestWindowFeature(Window.FEATURE_NO_TITLE); //will hide the title
        getSupportActionBar().hide();
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_prediction);
        textView = (TextView) findViewById(R.id.textView1);
        Bundle bundle = getIntent().getExtras();

        //Extract the data…
        final String emotion = bundle.getString("emotion");

        switch(emotion)
        {
            case "0":
                textView.setText("You seem so Neutral :-|");
                break;
            case "1":
                textView.setText("Yayyy! You are happy :) ");
                break;
            case "2":
                textView.setText("Ah :( Smile please");
                break;
            case "3":
                textView.setText("Chill . Cool down :P");
                break;
            case "4":
                textView.setText("Be Brave (^_-)");
                break;
        }




    }
    @Override
    public void onBackPressed() {
        startActivity(new Intent(this, MainActivity.class));
    }
}