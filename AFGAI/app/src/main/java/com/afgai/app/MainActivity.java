package com.afgai.app;

import android.app.Activity;
import android.os.Bundle;
import android.Manifest;
import android.content.Intent;
import android.net.Uri;
import android.webkit.ValueCallback;
import android.webkit.WebView;
import android.webkit.WebSettings;
import android.webkit.WebChromeClient;
import android.webkit.PermissionRequest;
import android.webkit.JavascriptInterface;
import android.content.pm.PackageManager;
import android.speech.tts.TextToSpeech;
import java.util.Locale;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.AuthCredential;
import com.google.firebase.auth.GoogleAuthProvider;

import com.google.android.gms.auth.api.signin.GoogleSignIn;
import com.google.android.gms.auth.api.signin.GoogleSignInClient;
import com.google.android.gms.auth.api.signin.GoogleSignInOptions;
import com.google.android.gms.common.api.ApiException;

public class MainActivity extends Activity {

    WebView webView;

    private ValueCallback<Uri[]> uploadMessage;
    private static final int FILE_CHOOSER = 100;
    private static final int GOOGLE_LOGIN = 200;

    FirebaseAuth auth;
    GoogleSignInClient googleClient;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);


        auth = FirebaseAuth.getInstance();

GoogleSignInOptions options =
        new GoogleSignInOptions.Builder(
                GoogleSignInOptions.DEFAULT_SIGN_IN)

        .requestEmail()
        .requestIdToken(getString(R.string.default_web_client_id))
        .build();


googleClient = GoogleSignIn.getClient(this, options);



webView = new WebView(this);

WebSettings settings = webView.getSettings();

settings.setJavaScriptEnabled(true);
settings.setDomStorageEnabled(true);
settings.setAllowFileAccess(true);
settings.setAllowContentAccess(true);
settings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);

webView.addJavascriptInterface(
        new Object(){

            @JavascriptInterface
            public void googleLogin(){

                Intent intent =
                        googleClient.getSignInIntent();

                startActivityForResult(
                        intent,
                        GOOGLE_LOGIN);
            }

@JavascriptInterface
public void startCall(){

    runOnUiThread(() -> {

        android.speech.SpeechRecognizer recognizer =
                android.speech.SpeechRecognizer.createSpeechRecognizer(
                        MainActivity.this
                );

        android.content.Intent intent =
                new android.content.Intent(
                        android.speech.RecognizerIntent.ACTION_RECOGNIZE_SPEECH
                );

        intent.putExtra(
                android.speech.RecognizerIntent.EXTRA_LANGUAGE,
                "ps-AF"
        );

        recognizer.startListening(intent);

    });

}

@JavascriptInterface
public void speak(String text){

    final TextToSpeech[] tts = new TextToSpeech[1];

    tts[0] = new TextToSpeech(MainActivity.this, status -> {

        if(status == TextToSpeech.SUCCESS){

Locale locale = new Locale("ps", "AF");
tts[0].setLanguage(locale);
tts[0].setSpeechRate(0.9f);
tts[0].setPitch(1.0f);
            tts[0].speak(
                    text,
                    TextToSpeech.QUEUE_FLUSH,
                    null,
                    "AFG_AI"
            );
        }

    });

}

        },
        "Android"
);


        webView.setWebChromeClient(new WebChromeClient(){


            @Override
            public boolean onShowFileChooser(
                    WebView view,
                    ValueCallback<Uri[]> callback,
                    FileChooserParams params){

                uploadMessage = callback;

                Intent intent =
                        params.createIntent();

                startActivityForResult(
                        intent,
                        FILE_CHOOSER);

                return true;
            }


            @Override
            public void onPermissionRequest(
                    PermissionRequest request){

                runOnUiThread(() ->
                        request.grant(
                        request.getResources()));

            }

        });


if (auth.getCurrentUser() != null) {

    webView.loadUrl(
    "file:///android_asset/index.html");

} else {

    webView.loadUrl(
    "file:///android_asset/welcome.html");

}

        setContentView(webView);


        if(android.os.Build.VERSION.SDK_INT >= 23){

            requestPermissions(
                    new String[]{
                    Manifest.permission.RECORD_AUDIO
                    },
                    10);
        }

    }



    @Override
    protected void onActivityResult(
            int requestCode,
            int resultCode,
            Intent data){

        super.onActivityResult(
                requestCode,
                resultCode,
                data);

if(requestCode == GOOGLE_LOGIN){

    try{

        com.google.android.gms.auth.api.signin
        .GoogleSignInAccount account =
        GoogleSignIn
        .getSignedInAccountFromIntent(data)
        .getResult(ApiException.class);


        AuthCredential credential =
        GoogleAuthProvider
        .getCredential(
        account.getIdToken(),
        null);


        auth.signInWithCredential(credential)
        .addOnSuccessListener(authResult -> {

            String uid = authResult.getUser().getUid();

            webView.evaluateJavascript(
                "localStorage.setItem('afg_user_id','" + uid + "');" +
                "window.location.href='index.html';",
                null
            );

        })
        .addOnFailureListener(e -> {

        });


    }catch(Exception e){

    }

}



        if(requestCode == FILE_CHOOSER){

            if(uploadMessage != null){

                Uri[] result=null;

                if(resultCode==RESULT_OK &&
                   data!=null){

                    result=new Uri[]{
                    data.getData()
                    };

                }

                uploadMessage.onReceiveValue(result);

                uploadMessage=null;
            }
        }
    }

}
