import { Component } from '@angular/core';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { PokemonService } from '../services/pokemon.service';
import {MatTableModule} from '@angular/material/table';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-pokemon',
  standalone: true,
  imports: [MatFormFieldModule, MatInputModule, MatButtonModule, FormsModule, MatTableModule, CommonModule, MatCardModule],
  templateUrl: './pokemon.component.html',
  styleUrl: './pokemon.component.scss'
})
export class PokemonComponent {
  pokemon_info: any[] = [];
  pokemon_name: string = '';
  displayedColumns: string[] = ['pokemon', 'move', 'type', 'generation', 'image_url'];

  constructor(private pokemonService: PokemonService) { }

  ngOnInit() {
    console.log("Pokemon component initialized");
  }


searchPokemon() {
  if (this.pokemon_name.trim()) {
    this.pokemonService.getPokemons(this.pokemon_name).subscribe({
      next: (data) => {
        const newData = Array.isArray(data) ? data : [data];
        // Check for duplicates before adding
        const newPokemon = newData.filter(newPoke => 
          !this.pokemon_info.some(existingPoke => 
            existingPoke.pokemon.toLowerCase() === newPoke.pokemon.toLowerCase()
          )
        );
        
        this.pokemon_info = [...this.pokemon_info, ...newPokemon];
        // Clear the input after successful search
        this.pokemon_name = '';
      },
      error: (error) => {
        console.error("Error fetching pokemon:", error);
      }
    });
  }
}


  cleanTable() {
    //remove all the data from the table
    this.pokemon_info = [];
    //load all the data from the database
    //this.loadAllPokemon();
    //clear the search field
    this.pokemon_name = '';
    //clear the search field

  }



}
