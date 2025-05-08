import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class PokemonService {
  private apiUrl= "http://localhost:5000";
  constructor(private http: HttpClient) { }
  getPokemons(pokemonName: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/pokemon/${pokemonName}`);
  }

  
}
