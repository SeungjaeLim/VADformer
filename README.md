# VADformer

VADformer is a backend service for the P.EYE XR project. It is designed to perform VAD (Valence-Arousal-Dominance) analysis using transfer learning with BERT (Bidirectional Encoder Representations from Transformers).

## Development

To get started with developing VADformer, follow these steps:

1. Clone the VADformer repository to your local machine:

```bash
git clone https://github.com/SeungjaeLim/VADformer.git
```

2. Create a conda environment using the `environment.yaml` file:

```bash
conda env create --file environment.yaml
```

3. Activate the conda environment:

```bash
conda activate VADformer
```


4. Run the `app.py` file to start the backend service:

```bash
python src/app.py
```

5. You can access the documentation for the API by visiting [http://localhost:80](http://localhost:80) in your web browser.

## API Endpoints

The VADformer API provides the following endpoints:

### `GET /VAD`

Returns a random VAD score as a JSON object with the format:

```json
{
  "VAD score": [0.123, 0.456, 0.789]
}
```
The VAD score is a list of three floats between 0 and 1, representing the valence, arousal, and dominance of an emotion.

### `POST /VAD`

Saves a response string to a list of responses. The response string should be provided in the request body as plain text.

The response is a JSON object with a message indicating whether the response was saved successfully:

```json
{
  "message": "Response \"This is a response.\" saved successfully."
}
```

## Contributors
Seungjae Lim (seungjaelim@kaist.ac.kr)
